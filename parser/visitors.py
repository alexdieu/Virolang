# parser/visitors.py
from antlr4.tree.Tree import ParseTreeVisitor
from .VirolangParser import VirolangParser
from molecular_models.models import Virus, Genome, Protein
from molecular_models.functions import optimized_reverse_translate, fetch_genome_from_ncbi
from cellular_models.cell import Host
from population_models.population import Population

class ExecutionVisitor(ParseTreeVisitor):
    def __init__(self, env: dict):
        self.env = env
        self.plot_data = None

    def visitAssignment(self, ctx: VirolangParser.AssignmentContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.env[name] = value
        print(f"Defined '{name}' as {type(value).__name__}")
        return value

    def visitCreateExpr(self, ctx:VirolangParser.CreateExprContext):
        obj_type = ctx.type_().getText()
        params = self._parse_params(ctx.param())
        if obj_type == "population":
            return Population(**params)
        # Handle other types if necessary
        raise ValueError(f"Unknown type to create: {obj_type}")

    def visitDesignExpr(self, ctx:VirolangParser.DesignExprContext):
        params = self._parse_params(ctx.param())
        protein_seq = params.get("protein", "M*")
        rna_seq = optimized_reverse_translate(protein_seq)
        genome = Genome(sequence=str(rna_seq), type="ssRNA+", definition=f"Designed for {protein_seq}")
        return Virus(name=params.get("name", "DesignedVirus"), genome=genome)

    def visitLoadGenomeExpr(self, ctx:VirolangParser.LoadGenomeExprContext):
        params = self._parse_params(ctx.param()) # This was causing the error
        accession_id = params.get('id')
        if not accession_id: raise ValueError("`load_genome` requires an `id` parameter.")
        record = fetch_genome_from_ncbi(accession_id, self.env['email'])
        genome = Genome(sequence=str(record.seq).replace("T", "U"), type='ssRNA+', definition=record.description)
        return Virus(name=record.name, genome=genome)

    def visitCalibrateExpr(self, ctx:VirolangParser.CalibrateExprContext):
        population = self.visit(ctx.expression())
        if not isinstance(population, Population):
            raise TypeError("Calibration can only be applied to a Population object.")
        params = self._parse_params(ctx.param()) # This was also causing the error
        population.calibrate(**params)
        return population

    def visitInfectExpr(self, ctx:VirolangParser.InfectExprContext):
        obj1 = self.visit(ctx.expression(0))
        obj2 = self.visit(ctx.expression(1))
        if isinstance(obj1, Virus) and isinstance(obj2, Population):
            pop = obj2
            pop.seed_infection(obj1, num_infected=1)
            for i in range(20):
                print(f"\n--- Running Population Cycle {i+1}/20 ---")
                pop.run_spread_cycle()
            self.plot_data = pop.history
            return pop.history
        raise TypeError("Infection operator '!' requires a Virus and a Population.")

    def visitIdExpr(self, ctx:VirolangParser.IdExprContext):
        name = ctx.ID().getText()
        if name not in self.env:
            raise NameError(f"Variable '{name}' is not defined.")
        return self.env[name]

    def _parse_params(self, params_ctx):
        """
        CORRECTED: This function now handles both single and multiple parameters.
        """
        params = {}
        # If params_ctx is not a list, wrap it in one so the loop works.
        param_list = params_ctx if isinstance(params_ctx, list) else [params_ctx]
        
        for p_ctx in param_list:
            if p_ctx: # Check that the parameter context exists
                key = p_ctx.ID().getText()
                value = self._eval_value(p_ctx.value())
                params[key] = value
        return params

    def _eval_value(self, val_ctx: VirolangParser.ValueContext):
        if val_ctx.STRING():
            return val_ctx.STRING().getText().strip('"')
        if val_ctx.NUMBER():
            num_str = val_ctx.NUMBER().getText()
            return int(num_str) if '.' not in num_str else float(num_str)
        if val_ctx.BOOL():
            return val_ctx.BOOL().getText() == 'true'
        if val_ctx.ID():
            return self.env.get(val_ctx.ID().getText())
        if val_ctx.value():
            return [self._eval_value(v) for v in val_ctx.value()]
        return None
