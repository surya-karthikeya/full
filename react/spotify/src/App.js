import React, { useState } from 'react';
import axios from 'axios';


function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [results1, setResults1] = useState([]);

  const handleInputChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSearch = async () => {
  const response = await axios.get(`http://localhost:5000/spotify/search?query=${query}`);
  let something = response['data']['item']['data']
  setResults(something);
  let something1 = response['data']['item']['image']
  setResults1(something1)

  console.log(something)
  };


  return (
    <div>
      <input type="text" value={query} onChange={handleInputChange} />
      <button onClick={handleSearch}>Search</button>

      <ul>
      {results.map((value, index) => (
          <li key={index}>
            {value} == <img src={results1[index]} />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Search;
