# 目录结构
```text
react-agent/
├── main.py                  # 入口
├── agent/
│   ├── loop.py              # ReAct 主循环
│   ├── prompt.py            # 提示词构建 / Action 解析
│   └──types.py             # HistoryItem 定义
├── tools/
│   ├── calculator.py
│   ├── current_time.py
│   ├── word_count.py
│   └── types.py             # Tool 定义
├── llm.py                   # 模型调用 + JSON 日志 + print_message / print_messages
├── requirements.txt
├── .env.example
└── README.MD
```

# 配置apikey
```bash
cp .env.example .env
```

# 运行
```bash
pip install -r requirements.txt
```

```bash
python main.py
```
