import os
import csv

def save_experiment_data(result_dir, experiment_settings, hidden_states):
    # ディレクトリが存在しない場合は作成
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    # 実験設定を .txt ファイルに保存
    with open(os.path.join(result_dir, "experiment_settings.txt"), "w") as f:
        f.write(str(experiment_settings))

    # 中間 activation を CSV ファイルに保存
    for i, hidden_state in enumerate(hidden_states):
        layer_name = f"layer_{i}"
        filename = os.path.join(result_dir, f"{layer_name}_activation.csv")
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(hidden_state.shape)  # shape を保存
            writer.writerows(hidden_state.reshape(hidden_state.shape[0], -1))  # 2次元にreshapeして保存
