<?php
// 读取 JSON 数据
$jsonData = file_get_contents('data.json');
$data = json_decode($jsonData, true);

// 检查是否有 uuid 参数
if (isset($_GET['uuid'])) {
    $requestedUuid = $_GET['uuid'];
    $foundItem = null;

    // 查找对应 uuid 的数据
    foreach ($data as $item) {
        if ($item['uuid'] === $requestedUuid) {
            $foundItem = $item;
            break;
        }
    }

    if ($foundItem) {
        // 替换 cover_image_url 的值
        $foundItem['cover_image_url'] = 'https://images.eallion.com/neodb/movie/random/cover/' . $foundItem['uuid'] . '.webp';

        // 返回对应的 JSON 数据
        header('Content-Type: application/json');
        echo json_encode($foundItem);
    } else {
        // 如果未找到对应的 uuid，返回 404 错误
        http_response_code(404);
        echo "UUID not found";
    }
} else {
    // 检查是否有 type 参数
    if (isset($_GET['type']) && $_GET['type'] === 'json') {
        // 随机选择一条数据
        $randomIndex = array_rand($data);
        $randomItem = $data[$randomIndex];

        // 替换 cover_image_url 的值
        $randomItem['cover_image_url'] = 'https://images.eallion.com/neodb/movie/random/cover/' . $randomItem['uuid'] . '.webp';

        // 返回完整的 JSON 数据
        header('Content-Type: application/json');
        echo json_encode($randomItem);
    } else {
        // 随机选择一个 uuid
        $randomIndex = array_rand($data);
        $randomUuid = $data[$randomIndex]['uuid'];

        // 返回纯文本的 uuid
        header('Content-Type: text/plain');
        echo $randomUuid;
    }
}
?>