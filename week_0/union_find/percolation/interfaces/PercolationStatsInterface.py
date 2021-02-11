
class PercolationStatsMeta(type):
    """
    A Percolation Stats metaclass that will be used for percolation stats class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'mean') and
                callable(subclass.mean) and
                hasattr(subclass, 'standard_deviation') and
                callable(subclass.standard_deviation) and
                hasattr(subclass, 'confidence_low') and
                callable(subclass.confidence_low) and
                hasattr(subclass, 'confidence_high') and
                callable(subclass.confidence_high))


class PercolationStatsInterface(metaclass=PercolationStatsMeta):

    def mean(self) -> float:
        """
        Sample mean of percolation threshold
        """
        pass

    def standard_deviation(self) -> float:
        pass

    def confidence_low(self) -> float:
        """
        Low endpoint of the 95% confidence interval
        """
        pass

    def confidence_high(self) -> float:
        """
        High endpoint of the 95% confidence interval
        """
        pass
