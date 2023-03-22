function search() {
  var query = document.getElementById('query').value;
  var xhr = new XMLHttpRequest();
  var resultList = document.getElementById('results')
  url='spotify/search?query=' + query;
  xhr.open('GET', url, true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === xhr.DONE && xhr.status === 200) {
    var results = JSON.parse(xhr.responseText);
      if (results.success) {
           newListHTML = results.item.data.map((item, image) => `<li>${item} ==>> <img src=${results.item.image[image]}></li>`);
//         dict = results.item
//         newListHTML = Object.keys(dict).map((item) => `<li>${item} ==>> <img src=${dict[item]}></li>`);
           resultList.innerHTML = newListHTML.join('');
      }
      else{
           resultList.innerHTML = 'Error occurred';
      }
    }
  };
  xhr.send();
}
