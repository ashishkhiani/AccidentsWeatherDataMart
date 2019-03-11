Design Decisions

1. Inspired by original weather data, we'll be maintaining a flag for every column with either {A (available), NA (not available), E (estimated)}
    *Estimated is only ever to be inherited from the weather data, and will never be manually set
2. The tables will all be loaded/cleaned with all the overlapping data self contained and will be split according to matches once added