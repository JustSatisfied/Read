const { spawn } = require('child_process');

// 要执行的 Python 脚本及参数
const pythonProcess = spawn('python', ['jiaoyi.py', 'arg1', 'arg2']);

// 监听 Python 进程的输出
pythonProcess.stdout.on('data', (data) => {
  console.log(`Python 输出：${data}`);
});

// 监听 Python 进程的错误输出
pythonProcess.stderr.on('data', (data) => {
  console.error(`Python 错误输出：${data}`);
});

// 监听 Python 进程的关闭事件
pythonProcess.on('close', (code) => {
  console.log(`Python 进程已关闭，退出码 ${code}`);
});