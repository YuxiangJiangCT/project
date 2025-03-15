import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RunSelector = ({ onSelectRun, selectedRunId }) => {
  const [runs, setRuns] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchRuns = async () => {
      try {
        setLoading(true);
        const response = await axios.get('http://localhost:8000/runs');
        setRuns(response.data);
        setLoading(false);
      } catch (error) {
        setError('Error fetching runs');
        setLoading(false);
        console.error('Error fetching runs:', error);
      }
    };

    fetchRuns();
  }, []);

  if (loading) {
    return <div className="text-center py-4">Loading runs...</div>;
  }

  if (error) {
    return <div className="text-red-500 text-center py-4">{error}</div>;
  }

  if (runs.length === 0) {
    return <div className="text-center py-4">No runs available. Please upload a file first.</div>;
  }

  return (
    <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <h2 className="text-xl font-bold mb-4">Select Run</h2>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="run">
          Run ID
        </label>
        <select
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="run"
          value={selectedRunId || ''}
          onChange={(e) => onSelectRun(e.target.value)}
        >
          <option value="">Select a run</option>
          {runs.map((run) => (
            <option key={run.run_id} value={run.run_id}>
              {run.client_name} - {run.run_id}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
};

export default RunSelector; 