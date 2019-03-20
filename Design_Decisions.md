Design Decisions

1. Inspired by original weather data, we'll be maintaining a flag for every column with either {A (available), NA (not available), E (estimated)}
    *Estimated is only ever to be inherited from the weather data, and will never be manually set
2. The tables will all be loaded/cleaned with all the overlapping data self contained and will be split according to matches once added
3. Though all cities were to be included, to be correlated with weather data, Calgary proved to have no capability to do so. The extremely sparse and poorly labelled
	data lead, with the lack of a time component, the accidents of Calgary could not be linked to an individual time and were only provided separated by day. The final
	decision was to completely remove the city's data as it is what the definition of "garbage data" refers to.