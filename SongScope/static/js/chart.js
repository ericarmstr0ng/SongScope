var endpoint = '/chart/data'
var defaultData = []
var labels = [];

$.ajax({
    method: "GET",
    ul: endpoint,
    success: function (data) {
        labels = data.labels;
        defaultData = data.default;
        var ctx = document.getElementById('myChart').getContext('2d');
        var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'line',

            // The data for our dataset
            data: {
                labels: labels,
                datasets: [{
                    label: labels,
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: [0, 10, 5, 2, 20, 30, 45]
                }]
            },

            // Configuration options go here
            options: {}
        });
    },


    error: function (error) {
        console.log(error)
    },

    });