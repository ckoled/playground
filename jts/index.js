const axios = require("axios").default;

const options = {
  method: 'GET',
  url: 'https://aerodatabox.p.rapidapi.com/health/services/feeds/FlightSchedules/airports',
  headers: {
    'X-RapidAPI-Host': 'aerodatabox.p.rapidapi.com',
    'X-RapidAPI-Key': '0037920bb1msh7e448a635989d78p138d01jsn4b7e7f35cba9'
  }
};

for (let i=0;i<100;i++) {
  axios.request(options).then(function (response) {
    console.log(response.status);
  }).catch(function (error) {
    console.error(error.response.status);
  });
}
