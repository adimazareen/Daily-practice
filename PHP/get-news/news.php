<!DOCTYPE html>
<html>
<head>
    <title>Simple Indian News Feed</title>
</head>
<body>
    <h2>Latest Indian News Headlines</h2>
    <?php
    // Indian news RSS feed URL (Times of India)
    $feed = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms";
    $rss = simplexml_load_file($feed);
    echo "<ul>";
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
