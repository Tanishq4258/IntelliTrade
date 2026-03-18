const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Default route to serve the dashboard
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start the Express server
app.listen(PORT, () => {
    console.log(`=========================================`);
    console.log(`IntelliTrade Frontend running successfully!`);
    console.log(`➜ Dashboard: http://localhost:${PORT}`);
    console.log(`=========================================`);
    console.log(`Ensure your Python backend is running at http://localhost:5000`);
});
