import json
import urllib.request

from jinja2 import Template

tmpl = """
<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['timeline']});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var container = document.getElementById('timeline');
        var chart = new google.visualization.Timeline(container);
        var dataTable = new google.visualization.DataTable();

        dataTable.addColumn({ type: 'string', id: 'Name' });
        dataTable.addColumn({ type: 'date', id: 'Start' });
        dataTable.addColumn({ type: 'date', id: 'End' });
        dataTable.addRows([
          {% for prod in products %}
          {% set sdate = prod.dateOpen.split("-") %}
          {% set edate = prod.dateClose.split("-") %}
          [ '{{prod.name}}', new Date({{sdate[0]}}, {{sdate[1]}}, {{sdate[2]}}), new Date({{edate[0]}}, {{edate[1]}}, {{edate[2]}}) ],
          {%endfor %}
          ]);
        chart.draw(dataTable);
      }
    </script>
  </head>
  <body>
    <div id="timeline" style="height: 100%;"></div>
  </body>
</html>
"""

with urllib.request.urlopen(
    "https://raw.githubusercontent.com/codyogden/killedbygoogle/main/graveyard.json"
) as url:
    data = json.loads(url.read().decode())
t = Template(tmpl, trim_blocks=True, lstrip_blocks=True)
print(t.render(products=data))
