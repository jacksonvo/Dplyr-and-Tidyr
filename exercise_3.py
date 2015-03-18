movies %>% filter(votes > 500, year > 1994) %>% group_by(title, year) %>% 
summarise(rating)
#cannot figure out what the 'last' function does
#did not know how to group the genres together
#played arround with multiple functions such as mutate
#may come back to it
