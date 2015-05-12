window.draw_speed_chart = (data) ->
    margin =
      top: 20
      right: 20
      bottom: 30
      left: 50

    width = 600 - (margin.left) - (margin.right)
    height = 300 - (margin.top) - (margin.bottom)

    parseDate = d3.time.format.iso.parse

    x = d3.time.scale()
        .range([0, width])

    y = d3.scale.linear()
        .range([height, 0])

    xAxis = d3.svg.axis().scale(x).orient('bottom')
    yAxis = d3.svg.axis().scale(y).orient('left')

    line = d3.svg.line()
        .x((d) -> x d.date)
        .y((d) -> y d.mb_per_second)

    svg = d3.select('div#speed-chart')
        .style("width", width + margin.left + margin.right + "px")
      .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
      .append('g')
        .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')

    data.forEach (d) ->
        d.date = parseDate(d.date)
        d.mb_per_second = +d.mb_per_second

    x.domain d3.extent(data, (d) -> d.date)
    y.domain [0, Math.max(5, d3.max(data, (d) -> d.mb_per_second))]

    svg.append('g')
        .attr('class', 'x axis')
        .attr('transform', 'translate(0,' + height + ')')
        .call(xAxis)

    svg.append('g')
        .attr('class', 'y axis')
        .call(yAxis)
      .append('text')
        .attr('transform', 'rotate(-90)')
        .attr('y', -1 * (margin.left - 17))
        .attr('dy', '.71em')
        .attr('x', -1 * (height) / 2)
        .style('text-anchor', 'middle')
        .text 'Megabytes/s'

    svg.append('path')
        .datum(data).attr('class', 'line')
        .attr('d', line)

    # Draw the points w/ tooltips
    circles = svg.append('svg:g')
        .selectAll('.data-point')
        .data(data)

    circles
        .enter()
      .append('svg:circle')
        .attr('class', 'data-point')
        .style('opacity', 1)
        .attr('cx', (d) -> x(d.date))
        .attr('cy', (d) -> y(d.mb_per_second))
        .attr('r', 3)
        .attr('original-title', 'blah')

    $('svg circle').tipsy
        gravity: 'w'
        html: true
        title: ->
            time = d3.time.format("%-I:%M %p")(this.__data__.date)
            return "#{ this.__data__.mb_per_second } MB/s<br>#{ time }"
