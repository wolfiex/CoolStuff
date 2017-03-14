### Nesting: 
when you want to make an object into a nested dictionary (1 key multiple values) 
http://learnjsdata.com/group_data.html

    var nest  = d3.nest()
      .key(function(d) { return d.name; })
      .entries(expenses);

  ### Mapping
    var map = new Map(data.nodes.map(d=> [d.id,d]))
    map.get(261)
