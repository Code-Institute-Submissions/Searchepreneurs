var ctx = document.getElementById('seoLoadTimeChart');
var seoLoadTimeChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['2 seconds', '3 seconds', '4 seconds', '5 seconds', '6 seconds', '7 seconds'],
        datasets: [{
            label: 'bounce rate (%)',
            data: [9.6, 13, 17.1, 22.2, 27.4, 32.3],
            backgroundColor: [
                'rgba(0, 255, 0, 1)',
                'rgba(95, 166, 0, 1)',
                'rgba(171, 166, 0, 1)',
                'rgba(231, 145, 0, 1)',
                'rgba(231, 98, 0, 1)',
                'rgba(255, 0, 0, 1)',
            ],
            borderColor: [
                'rgba(0, 0, 0, 1)',
                'rgba(0, 0, 0, 1)',
                'rgba(0, 0, 0, 1)',
                'rgba(0, 0, 0, 1)',
                'rgba(0, 0, 0, 1)',
                'rgba(0, 0, 0, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
          scaleLabel: {
            display: true,
            labelString: 'Bounce rate (%)'
          }
        }],
        xAxes: [{
          scaleLabel: {
            display: true,
            labelString: 'Page load time (seconds)'
          }
        }],
        }
    }
});