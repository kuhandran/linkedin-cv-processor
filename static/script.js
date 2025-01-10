document.querySelector('form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    
    try {
        const response = await fetch('/upload-cv', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        alert('CV processed successfully! Check the console for details.');
        console.log(result);
    } catch (error) {
        alert('Error processing CV');
        console.error(error);
    }
});

