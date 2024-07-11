// document.addEventListener("DOMContentLoaded", function() {
//     fetchData();
//   });
  
//   async function fetchData() {
//     await fetch('https://www.overnightmountings.com/api/rest/itembom?page_number=1&number_of_items=30&category_id=134&diamond_quality=B')
//       .then(response => response.json())
//       .then(data => {
        
//         console.log(data);
//         // populateTable(data);
//       })
//       .catch(error => console.error('Error fetching data:', error));
//   }
//   fetchData();
//   

// async function fetchData() {
// fetch('https://api.example.com/datahttps://www.overnightmountings.com/api/rest/itembom?page_number=1&number_of_items=30&category_id=134&diamond_quality=B')
// .then(response => {
//   // Check if response is successful (status code 200)
//   if (!response.ok) {
//     throw new Error('Failed to fetch data');
//   }
//   // Parse the response body as JSON
//   return response.json();
// })
// .then(data => {
//   // Do something with the data
//   console.log(data);
// })
// .catch(error => {
//   // Handle any errors that occurred during the fetch
//   console.error('Error fetching data:', error);
// });
// }
// fetchData();


// let URL = "https://www.overnightmountings.com/api/rest/itembom?page_number=1&number_of_items=30&category_id=134&diamond_quality=B";
let url = "https://cat-fact.herokuapp.com/facts";
let factPara = document.getElementById("facts")

const getdata = async () => {
    console.log("getting data...");
    let response = await fetch(url);
    console.log(response);
    let data = await response.json();
    factPara.innerText = data[1].text;
}

// let promise = fetch('');
// console.log(promise);
// promise.then((value) => {
//     return value.json;
// })
// .then((value) => {
//     console.log(value);
// })
  