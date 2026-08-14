
<!DOCTYPE html>
<html>
<head>
    <title>Simple Web Feed</title>
</head>
<body>
    <h2>Simple Web Feed</h2>
    <?php
    // Basic feed URL
    $feed = "https://feeds.bbci.co.uk/news/rss.xml";
    // Fetch and parse the RSS feed
    $rss = simplexml_load_file($feed);
    echo "<ul>";
    // Show the first 5 headlines
    $count = 0;
    foreach ($rss->channel->item as $item) {
        if ($count == 5) break;
        echo "<li><a href='{$item->link}' target='_blank'>{$item->title}</a></li>";
        $count++;
    }
    echo "</ul>";
    ?>
</body>
</html>
