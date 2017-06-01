### Nesting: 
when you want to make an object into a nested dictionary (1 key multiple values) 
http://learnjsdata.com/group_data.html

    var nest  = d3.nest()
      .key(function(d) { return d.name; })
      .entries(expenses);

  ### Mapping
    var map = new Map(data.nodes.map(d=> [d.id,d]))
    map.get(261)


  ### dave electron
    # for use in npm scripts
    npm install electron-packager --save-dev

    # for use from cli
    npm install electron-packager -g
    
    npm install --save-dev electron
    electron-packager . --overwrite --platform=darwin --arch=x64 --icon=assets/icons/mac/icon.icns --prune=true --out=release-builds
