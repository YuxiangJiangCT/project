import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Plot from 'react-plotly.js';

const DataVisualization = ({ runId }) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!runId) return;

    const fetchData = async () => {
      try {
        setLoading(true);
        setError('');
        const response = await axios.get(`http://localhost:8000/data/${runId}`);
        setData(response.data);
        setLoading(false);
      } catch (error) {
        setError('Error fetching data');
        setLoading(false);
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [runId]);

  if (!runId) {
    return (
      <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 text-center">
        <p className="text-gray-600">Please select a run to visualize data</p>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 text-center">
        <p className="text-gray-600">Loading data...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
          <span className="block sm:inline">{error}</span>
        </div>
      </div>
    );
  }

  if (!data || !data.data || data.data.length === 0) {
    return (
      <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 text-center">
        <p className="text-gray-600">No data available for this run</p>
      </div>
    );
  }

  // Process data for plotting
  const parameters = [...new Set(data.data.map(item => item.parameter))];
  const plotData = parameters.map(param => {
    const filteredData = data.data.filter(item => item.parameter === param);
    const sortedData = filteredData.sort((a, b) => a.time_stamp - b.time_stamp);
    
    return {
      x: sortedData.map(item => item.time_stamp),
      y: sortedData.map(item => item.process_value),
      type: 'scatter',
      mode: 'lines',
      name: `${param} (${filteredData[0]?.units || ''})`,
    };
  });

  return (
    <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <h2 className="text-xl font-bold mb-4">
        Data Visualization - {data.client_name} ({data.run_id})
      </h2>
      <div className="w-full">
        <Plot
          data={plotData}
          layout={{
            title: 'Process Parameters vs Time',
            xaxis: {
              title: 'Time',
            },
            yaxis: {
              title: 'Process Value',
            },
            autosize: true,
            height: 500,
            legend: {
              orientation: 'h',
              y: -0.2
            }
          }}
          useResizeHandler={true}
          style={{ width: '100%', height: '100%' }}
        />
      </div>
    </div>
  );
};

export default DataVisualization; 