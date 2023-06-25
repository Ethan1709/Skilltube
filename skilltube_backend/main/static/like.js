document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-button');
  
    likeButtons.forEach(function(likeButton) {
      likeButton.addEventListener('click', function() {
        const videoId = this.dataset.videoId;
  
        // Make an AJAX request to add a like for the video ID
        fetch(`/video/${videoId}/add-like/`, {  // Update the URL with videoId
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
          },
          body: JSON.stringify({ video_id: videoId })
        })
        .then(response => response.json())
        .then(data => {
          // Handle the response or update the UI as needed
          console.log(data);
          // Update the like count in the UI
          const likeCountElement = document.getElementById(`like-count-${videoId}`);
          if (likeCountElement) {
            likeCountElement.textContent = data.like_count;
          }
        })
        .catch(error => {
          // Handle any errors
          console.error(error);
        });
      });
    });
  
    // Helper function to get the value of a cookie by name
    function getCookie(name) {
      const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
      return cookieValue ? cookieValue.pop() : '';
    }
  });
  