const socket  = io();
const context = document.getElementById('myChart').getContext('2d');

const data = {
    labels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    datasets: [{
        label: 'some random graph',
        data: [],
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
    }]
};

const config  = {
    type: 'line',
    data: data,
    options: {
        responsive: true
    }
};

const myChart = new Chart(context, config);

const updateChart = (newData = []) => {
    // update labels (x-achse)
    let labels = [...Array(myChart.data.labels.length + newData.length).keys()];
    myChart.data.labels = labels;

    // update data
    let data = [...myChart.data.datasets[0].data, ...newData];

    if (data?.length > 1000) {
        data = d;
    }
    myChart.data.datasets[0].data = data;


    myChart.update();
}

socket.on('connect', () => {
    socket.emit('mount');
})

socket.on('data', (data) => {
    updateChart(data);
})
