async function continueStory() {
   const input = document.getElementById('input').value;
   const response = await fetch('http://localhost:8000/generate', {
       method: 'POST',
       headers: {
           'Content-Type': 'application/json',
       },
       body: JSON.stringify({ prompt: input }),
   });

   const data = await response.json();
   const storyDiv = document.getElementById('story');
   storyDiv.innerText += data.story + '\n';
   document.getElementById('input').value = '';
}
