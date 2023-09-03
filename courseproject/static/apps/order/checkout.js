function isDoneMainOrder() {
    $.ajax({
      method: "PUT",
      url: is_done_url,
      headers: { "X-CSRFToken": csrftoken_ },
      data: {
        is_done: true,
      },
      dataType: "json",
      success: function (data) {
        console.log('is_done_url', is_done_url)
        window.location.href = home_url;
        console.log('success', data);
      },
      error: function(data) {
        console.log('error cixdiiiii', data);
      }
    });
  }