#list the 10 films under this certain year
movies %>% filter(votes > 500, rating > 8.0, year < 1926)
