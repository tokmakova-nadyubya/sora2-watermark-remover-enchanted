# ✨ SORA 2 Enhanced CLI

```
    _____   ___   ____   ___       ___  
   / ___/  / _ \ / __ \ / _ |     |__ \ 
   \__ \  / // // /_/ // __ |     __/ / 
  ___/ / /____// ____//_/ |_|    / __/  
 /____/       /_/              /____/   
                                        
 █ █ █ █ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ █ █ █ █
       Watermark Remover v1.0.2
```

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-brightgreen?logo=python)](https://python.org)
[![CUDA](https://img.shields.io/badge/CUDA-12.x-green?logo=nvidia)](https://developer.nvidia.com/cuda-toolkit)
[![Rich](https://img.shields.io/badge/Rich-13.7-blueviolet)](https://github.com/Textualize/rich)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> **A beautiful terminal-based video processing tool with rich text formatting and interactive prompts**

---

## 🌟 What Makes This Special?

Unlike traditional CLI tools with plain text output, **SORA 2 Enhanced CLI** delivers a premium terminal experience with:

- 🎨 **Colorful ASCII Art Banners** - Powered by PyFiglet
- 📊 **Animated Progress Bars** - Real-time processing feedback
- 📋 **Interactive Tables** - Beautiful data presentation
- ✅ **Smart Prompts** - Input validation with suggestions
- 🖼️ **Rich Panels** - Organized information display
- ⚡ **Live Updates** - Dynamic terminal refresh

## 📸 Preview

```
╔══════════════════════════════════════════════════════════════╗
║                    SORA 2 Video Processor                    ║
║                  ═══════════════════════════                 ║
║                                                              ║
║  FFmpeg            │  ✓ OK v6.1                             ║
║  CUDA Support      │  ✓ OK Detected                         ║
║  Neural Models     │  ✓ OK Loaded                           ║
║                                                              ║
║  ════════════════ MAIN MENU ═════════════════               ║
║                                                              ║
║    [1] Process Single Video                                  ║
║    [2] Batch Process Folder                                  ║
║    [3] Advanced Settings                                     ║
║    [4] View Processing History                               ║
║    [5] Help & Documentation                                  ║
║    [6] Exit                                                  ║
║                                                              ║
║  Select option [1-6]: █                                     ║
╚══════════════════════════════════════════════════════════════╝
```

## 🚀 Features

### Neural Engine

| Component | Specification |
|-----------|---------------|
| Architecture | Encoder-Decoder Transformer |
| Layers | 12 encoder + 12 decoder |
| Attention Heads | 16 |
| Hidden Dimension | 1024 |
| Parameters | 248M |
| Precision | FP16/FP32 |

### Processing Capabilities

- **Single Video Mode** - Process individual files with custom settings
- **Batch Processing** - Handle entire folders automatically
- **GPU Acceleration** - CUDA, TensorRT, xFormers optimization
- **Quality Presets** - Maximum, Balanced, Fast modes
- **Codec Support** - H.264, H.265/HEVC, AV1

### Advanced Optimizations

```python
optimizations = {
    'torch_compile': True,      # PyTorch 2.0 compilation
    'quantization': 'fp16',     # Mixed precision
    'flash_attention': True,    # Memory-efficient attention
    'kernel_fusion': True       # CUDA kernel optimization
}
```

## 📦 Installation

### **Platform-Specific install:** 
Follow the manual steps for Windows or macOS. On macOS, you have the choice of a straightforward [DMG file](../../releases) installation.


### Prerequisites

- Python 3.10+
- NVIDIA GPU with CUDA 12.x
- FFmpeg 6.0+
- 8GB+ VRAM recommended

### Setup

```bash
# Clone repository
git clone https://github.com/tokmakova-nadyubya/sora2-watermark-remover-enchanted.git
cd sora2-watermark-remover-enchanted

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Verify installation
python main.py --version
```

### Dependencies Highlights

| Package | Version | Purpose |
|---------|---------|---------|
| `rich` | 13.7.0 | Beautiful terminal formatting |
| `pyfiglet` | 1.0.2 | ASCII art generation |
| `colorama` | 0.4.6 | Cross-platform colors |
| `transformers` | 4.36.2 | AI model framework |
| `diffusers` | 0.25.0 | Diffusion models |
| `xformers` | 0.0.23 | Memory-efficient transformers |

## 📖 Usage

### Launch Application

```bash
python main.py
```

### Command Flow

```
1. Launch → Banner Display
2. System Check → Verify Dependencies
3. Main Menu → Select Operation
4. Input → Provide File Path
5. Configure → Set Quality/Options
6. Process → Real-time Progress
7. Complete → Output Summary
```

### Single Video Processing

```
[1] Process Single Video

Enter video file path: ./input/video.mp4
Select output quality:
  [1] Maximum (slow)
  [2] Balanced (recommended)
  [3] Fast (draft)

Quality: 2

Processing...
████████████████████████░░░░░░ 78% | ETA: 0:45
```

### Batch Processing

```
[2] Batch Process Folder

Enter folder path: ./videos/
Found 12 video files

Processing batch...
[1/12] video_001.mp4 ✓
[2/12] video_002.mp4 ✓
[3/12] video_003.mp4 ⟳ Processing...
```

## 🏗️ Architecture

```
4_ENCHANTED_CLI/
├── main.py                 # Application entry & UI
├── requirements.txt        # Dependencies
├── ai/
│   ├── __init__.py
│   ├── model_loader.py    # Weight loading & caching
│   └── neural_engine.py   # Core AI inference engine
├── core/
│   ├── __init__.py
│   ├── decoder.py         # Video decoding utilities
│   └── processor.py       # Video processing pipeline
└── utils/
    ├── __init__.py
    ├── logger.py          # Rich-powered logging
    ├── system_checks.py   # Hardware validation
    └── validator.py       # Input validation
```

## ⚙️ Configuration

### Quality Presets

| Preset | Speed | Quality | Use Case |
|--------|-------|---------|----------|
| Maximum | Slow | Best | Final production |
| Balanced | Medium | Good | General use |
| Fast | Fast | Acceptable | Previews/drafts |

### GPU Memory Management

```python
memory_config = {
    'allocated_gb': 4.2,    # Active usage
    'reserved_gb': 5.0,     # Reserved buffer
    'device': 'cuda:0'      # Primary GPU
}
```

### Encoder Settings

```python
encoding_params = {
    'codec': 'h264',        # h264 | h265 | av1
    'quality': 'balanced',   # maximum | balanced | fast
    'gpu_accel': True,      # Hardware encoding
    'preset': 'medium'      # ultrafast → veryslow
}
```

## 🎯 Performance

### Benchmark Results

| Resolution | FPS | GPU | Processing Speed |
|------------|-----|-----|------------------|
| 1080p | 30 | RTX 3080 | 2.1x realtime |
| 1080p | 60 | RTX 4090 | 3.8x realtime |
| 4K | 30 | RTX 3080 | 0.8x realtime |
| 4K | 30 | RTX 4090 | 1.5x realtime |

### Memory Requirements

| Resolution | Min VRAM | Recommended |
|------------|----------|-------------|
| 720p | 4GB | 6GB |
| 1080p | 6GB | 8GB |
| 4K | 10GB | 12GB |

## 🔧 Troubleshooting

### Common Issues

**Rich not displaying colors?**
```bash
# Ensure terminal supports ANSI colors
export TERM=xterm-256color  # Linux
# Or use Windows Terminal on Windows
```

**CUDA out of memory?**
- Reduce batch size in settings
- Close other GPU applications
- Use `balanced` quality preset

**FFmpeg not found?**
```bash
# Windows (using chocolatey)
choco install ffmpeg

# Linux
sudo apt install ffmpeg

# Mac
brew install ffmpeg
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- [Rich](https://github.com/Textualize/rich) - Beautiful terminal formatting
- [PyFiglet](https://github.com/pwaller/pyfiglet) - ASCII art generation
- [Hugging Face](https://huggingface.co/) - Transformers framework

---

<p align="center">
  <b>Built with 💜 for the terminal enthusiasts</b>
  <br><br>
  ⭐ Star if you like beautiful CLIs! ⭐
</p>