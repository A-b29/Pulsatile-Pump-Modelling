from physiology import CardiacModel
from solver import FlowSolver
from visualization import Visualizer


def main():

    cardiac = CardiacModel()

    solver = FlowSolver(cardiac)

    viz = Visualizer(solver)

    viz.animate()


if __name__ == "__main__":
    main()