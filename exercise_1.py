movies %>% filter(votes > 500, rating > 8.0) %>% summarise(n=n())
