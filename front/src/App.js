import React from 'react';
import logo from './static/query_stats_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
let baseHost = 'localhost';

function App() {
  return (
    <div className="App">
      <head>
        <link rel="icon" href={logo} type="image/x-icon" />
        <title>Plotly no React</title>
      </head>
      <button className="btn btn-primary" onClick={fetchData}>Gerar gráfico</button>
      <div id="data-container"></div>
    </div>
  );
}

async function fetchData() {
  try {
    const response = await fetch(`http://${baseHost}:1337/graph/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        title: 'foo',
        body: 'bar',
        userId: 1,
      }),
    });

    const data = await response.json();
    const container = document.getElementById('data-container');

    // Insere o HTML do Plotly diretamente
    if (data.html) {
      container.innerHTML = data.html;
    } else {
      container.innerHTML = '<p>error</p>';
    }

    // Se o HTML usa <script>, precisamos forçar a execução dos scripts
    const scripts = container.querySelectorAll('script');
    scripts.forEach((oldScript) => {
      const newScript = document.createElement('script');
      newScript.text = oldScript.text;
      oldScript.replaceWith(newScript);
    });

  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
    const container = document.getElementById('data-container');
    container.innerHTML = '<p>error</p>';
  }
}

export default App;
