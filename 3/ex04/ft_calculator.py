class calculator:
    """
    Claculator.
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Compute and print the dot product of two vectors..
        """
        dot_product = 0.0
        for i in V1:
            dot_product += i * V2[V1.index(i)]
        print(f"Dot product is: {int(dot_product)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        ACompute and print the sum of two vectors.
        """
        result = []
        for i in V1:
            result.append(i + V2[V1.index(i)])
        print(f"Add Vector is : {[f'{val:.1f}' for val in result]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Compute and print the difference of two vectors.
        """
        result = []
        for i in V1:
            result.append(i - V2[V1.index(i)])
        print(f"Sous Vector is: {[f'{val:.1f}' for val in result]}")
