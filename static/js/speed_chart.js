// Generated by CoffeeScript 1.6.3
(function() {
  window.draw_speed_chart = function(data) {
    var circles, height, line, margin, parseDate, svg, width, x, xAxis, y, yAxis;
    margin = {
      top: 20,
      right: 20,
      bottom: 30,
      left: 50
    };
    width = 600 - margin.left - margin.right;
    height = 300 - margin.top - margin.bottom;
    parseDate = d3.time.format.iso.parse;
    x = d3.time.scale().range([0, width]);
    y = d3.scale.linear().range([height, 0]);
    xAxis = d3.svg.axis().scale(x).orient('bottom');
    yAxis = d3.svg.axis().scale(y).orient('left');
    line = d3.svg.line().x(function(d) {
      return x(d.date);
    }).y(function(d) {
      return y(d.mb_per_second);
    });
    svg = d3.select('div#speed-chart').style("width", width + margin.left + margin.right + "px").append('svg').attr('width', width + margin.left + margin.right).attr('height', height + margin.top + margin.bottom).append('g').attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
    data.forEach(function(d) {
      d.date = parseDate(d.date);
      return d.mb_per_second = +d.mb_per_second;
    });
    x.domain(d3.extent(data, function(d) {
      return d.date;
    }));
    y.domain([
      0, d3.max(data, function(d) {
        return d.mb_per_second;
      })
    ]);
    svg.append('g').attr('class', 'x axis').attr('transform', 'translate(0,' + height + ')').call(xAxis);
    svg.append('g').attr('class', 'y axis').call(yAxis).append('text').attr('transform', 'rotate(-90)').attr('y', -1 * (margin.left - 12)).attr('dy', '.71em').attr('x', -1 * height / 2).style('text-anchor', 'middle').text('MB/s');
    svg.append('path').datum(data).attr('class', 'line').attr('d', line);
    circles = svg.append('svg:g').selectAll('.data-point').data(data);
    circles.enter().append('svg:circle').attr('class', 'data-point').style('opacity', 1).attr('cx', function(d) {
      return x(d.date);
    }).attr('cy', function(d) {
      return y(d.mb_per_second);
    }).attr('r', 3).attr('original-title', 'blah');
    return $('svg circle').tipsy({
      gravity: 'w',
      html: true,
      title: function() {
        var time;
        time = d3.time.format("%-I:%M %p")(this.__data__.date);
        return "" + this.__data__.mb_per_second + " MB/s<br>" + time;
      }
    });
  };

}).call(this);
