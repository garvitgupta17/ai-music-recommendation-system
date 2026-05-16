import random
from deap import base, creator, tools
from utils import compute_fitness


def run_ga(dataset, user_pref):

    if not hasattr(creator, "FitnessMax"):
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))

    if not hasattr(creator, "Individual"):
        creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()

    toolbox.register("attr_song", random.randint, 0, len(dataset)-1)

    toolbox.register(
        "individual",
        tools.initRepeat,
        creator.Individual,
        toolbox.attr_song,
        n=1
    )

    toolbox.register(
        "population",
        tools.initRepeat,
        list,
        toolbox.individual
    )

    def evaluate(ind):

        idx = ind[0]

        song = dataset.iloc[idx]

        return (compute_fitness(song,user_pref),)

    toolbox.register("evaluate",evaluate)

    toolbox.register("mate", tools.cxUniform, indpb=0.5)

    toolbox.register(
        "mutate",
        tools.mutUniformInt,
        low=0,
        up=len(dataset)-1,
        indpb=0.5
    )

    toolbox.register("select",tools.selTournament,tournsize=3)

    population = toolbox.population(n=100)

    for ind in population:
        ind.fitness.values = toolbox.evaluate(ind)

    fitness_history = []

    for gen in range(30):

        offspring = toolbox.select(population,len(population))
        offspring = list(map(toolbox.clone,offspring))

        for child1,child2 in zip(offspring[::2],offspring[1::2]):

            if random.random()<0.8:

                toolbox.mate(child1,child2)

                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:

            if random.random()<0.2:

                toolbox.mutate(mutant)

                del mutant.fitness.values

        invalid = [ind for ind in offspring if not ind.fitness.valid]

        for ind in invalid:

            ind.fitness.values = toolbox.evaluate(ind)

        population[:] = offspring

        best = max(population,key=lambda x:x.fitness.values[0])

        fitness_history.append(best.fitness.values[0])

    population.sort(
    key=lambda x: x.fitness.values[0],
    reverse=True
)

    seen = set()
    recommendations = []

    for ind in population:

        idx = ind[0]

        if idx not in seen:

            recommendations.append(dataset.iloc[idx])

            seen.add(idx)

        if len(recommendations) == 10:
            break

    return recommendations, fitness_history