// custom javascript for d3 visualizations

  d3.json('http://localhost:8000/getJobsfrequency', function(data) {

    for(var key in data){ data[key]['time'] = new Date(data[key]['time'] *1000) }

    //debugger
    //data = MG.convert.date(data, new Date('time' *1000));
    MG.data_graphic({
        title: "Line Chart",
        description: "Jobs running at given instance.",
        data: data,
        width: 960,
        height: 520,
        right: 40,
        target: '#chart',
        x_accessor: 'time',
        y_accessor: 'value',
        interpolate: 'monotone'
    });
  });

  createJobs()


function createJobs() {

var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

//var x = d3.scale.ordinal()
//    .rangeRoundBands([0, width], .1);

var x = d3.scale.linear()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

var svg = d3.select("#chart2").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.json('http://localhost:8000/getJobsfrequency', function(error,data) {
  if (error) throw error;

  for(var key in data){ data[key]['time'] = new Date(data[key]['time'] *1000) }

  x.domain([d3.min(data, function(d) { return d['time']; }), d3.max(data, function(d) { return d['time']; })]);
  y.domain([0, d3.max(data, function(d) { return d['value']; })]);

  var formatTime = function(d) {
    
    str = new Date(d *1000);
    str = str.toString();
    final = str.substring(4,25);
    return final;      
  }

  var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
    .tickFormat(formatTime);

  var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");


  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Jobs");

  svg.selectAll(".bar")
      .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d['time']); })
      .attr("width", 5)
      .attr("y", function(d) { return y(d['value']); })
      .attr("height", function(d) { return height - y(d['value']); });
});

function type(d) {
  d['value'] = +d['value'];
  return d;
}


} // function ends


