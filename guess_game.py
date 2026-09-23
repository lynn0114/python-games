import random

print("🎮 欢迎来到猜数字游戏！")
print("请选择难度：")
print("1. 简单（1-50，10次机会）")
print("2. 中等（1-100，7次机会）")
print("3. 困难（1-200，5次机会）")

while True:
    try:
        level = int(input("请输入难度编号（1/2/3）："))
        if level in [1, 2, 3]:
            break
        print("❌ 请输入 1、2 或 3！")
    except ValueError:
        print("❌ 输入无效，请输入整数。")

if level == 1:
    max_num, max_attempts = 50, 10
elif level == 2:
    max_num, max_attempts = 100, 7
else:
    max_num, max_attempts = 200, 5

answer = random.randint(1, max_num)
print(f"\n🎯 请在 1 到 {max_num} 之间猜一个数字。")
print(f"🎮 你有 {max_attempts} 次机会。")

for attempt in range(1, max_attempts + 1):
    while True:
        try:
            guess = int(input(f"\n👉 第 {attempt} 次猜，请输入数字："))
            if 1 <= guess <= max_num:
                break
            print(f"🚫 请输入 1 到 {max_num} 之间的数字。")
        except ValueError:
            print("🚫 输入无效，请输入整数。")

    if guess == answer:
        print(f"🎉 恭喜你，猜对了！答案就是 {answer}。")
        break
    elif guess < answer:
        print("📈 猜小了！")
    else:
        print("📉 猜大了！")
else:
    print(f"\n😢 游戏结束，{max_attempts} 次机会已用完。正确答案是 {answer}。")

    # TODO: 记录玩家最高分
    # 测试新功能