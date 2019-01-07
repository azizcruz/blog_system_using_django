$(document).ready(function() {
  // Handle delete post.
  $("#delete-post").on('click', function(e) {
    var ans = confirm("Are you sure you want to delete this post ?")

    if(!ans) {
      e.preventDefault();
      return false;
    }

  })
});
