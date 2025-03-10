$( document ).on('click', '#categories', function(event) {
    console.log('Step 1');
    $.ajax({
                url: '/api/v0/categories/',
                success: function (data) {
                    // data - ответ от сервера
                    console.log('Step 2')
                    console.log(data);
                    for (i = 0; i < data.length; i++) {
                        // словарь
                       item = data[i];
                       name = item.name;
                       console.log(name);
                       $('#div_categories').append('<li>' + name + '</li>' );
                    }
                },
            });
});

$( document ).on('click', '#posts', function(event) {
    console.log('Step 1');
    $.ajax({
                url: '/api/v0/posts/',
                success: function (data) {
                    // data - ответ от сервера
                    console.log('Step 2')
                    console.log(data);
                    for (i = 0; i < data.length; i++) {
                        // словарь
                       item = data[i];
                       name = item.name;
                       console.log(name);
                       $('#div_posts').append('<li>' + name + '</li>' );
                    }
                },
            });
});

$( document ).on('click', '#all', function(event) {
    $.ajax({
                url: '/api/v0/categories/',
                success: function (data) {
                    console.log(data);
                    for (i = 0; i < data.length; i++) {
                       item = data[i];
                       name = item.name;
                       console.log(name);
                       $('#div_categories').append('<li>' + name + '</li>' );
                    }
                },
            });
    $.ajax({
                url: '/api/v0/posts/',
                success: function (data) {
                    console.log(data);
                    for (i = 0; i < data.length; i++) {
                       item = data[i];
                       name = item.name;
                       console.log(name);
                       $('#div_posts').append('<li>' + name + '</li>' );
                    }
                },
            });
});