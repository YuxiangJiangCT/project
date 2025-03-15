import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import RunSelector from './components/RunSelector';
import DataVisualization from './components/DataVisualization';

function App() {
  const [selectedRunId, setSelectedRunId] = useState('');

  const handleUploadSuccess = (runId) => {
    setSelectedRunId(runId);
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-blue-600 text-white shadow">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-3xl font-bold">Boston Bioprocess Data Visualization</h1>
        </div>
      </header>
      
      <main className="container mx-auto px-4 py-6">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="md:col-span-1">
            <FileUpload onUploadSuccess={handleUploadSuccess} />
            <RunSelector 
              onSelectRun={setSelectedRunId} 
              selectedRunId={selectedRunId} 
            />
          </div>
          <div className="md:col-span-2">
            <DataVisualization runId={selectedRunId} />
          </div>
        </div>
      </main>
      
      <footer className="bg-gray-200 py-4">
        <div className="container mx-auto px-4 text-center text-gray-600">
          <p>Boston Bioprocess Data Visualization Tool</p>
        </div>
      </footer>
    </div>
  );
}

export default App; 