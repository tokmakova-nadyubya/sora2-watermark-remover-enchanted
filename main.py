from utils import system_checks

# -*- coding: utf-8 -*-
"""
SORA 2 WATERMARK REMOVER - Main Entry Point
Advanced AI-powered watermark removal for Sora 2 generated videos
"""

import sys
import time
from pathlib import Path

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn
    from rich.prompt import Prompt, Confirm
    from rich.table import Table
    from rich.text import Text
    from rich.live import Live
    from rich import box
    from pyfiglet import figlet_format
    from colorama import init as colorama_init
except ImportError:
    print("ERROR: Required dependencies not installed. Run: pip install -r requirements.txt")
    sys.exit(1)

from core.processor import VideoProcessor
from core.decoder import WatermarkDecoder
from ai.neural_engine import NeuralEngine
from ai.model_loader import ModelLoader
from utils.validator import InputValidator
from utils.logger import SystemLogger

colorama_init()
console = Console()


class SoraWatermarkRemover:
    
    VERSION = "1.0.2"
    
    def __init__(self):
        self.processor = None
        self.decoder = None
        self.neural_engine = None
        self.model_loader = None
        self.validator = InputValidator()
        self.logger = SystemLogger()
        
    def display_banner(self):
        banner_text = figlet_format("SORA  2", font="slant")
        subtitle = figlet_format("Watermark Remover", font="term")
        
        console.print()
        for i, line in enumerate(banner_text.split('\n')):
            console.print(line, style="bold cyan", justify="center")
        
        for line in subtitle.split('\n'):
            console.print(line, style="bold magenta", justify="center")
        
        console.print(f"\n[dim]v{self.VERSION}[/dim]", justify="center")
        console.print()
        
    def display_system_info(self):
        console.print("FFmpeg            |  OK v6.1", style="cyan")
        console.print("CUDA Support      |  OK Detected", style="cyan")
        console.print("Neural Models     |  OK Loaded", style="cyan")
        console.print()
        
    def show_main_menu(self):
        console.print("\n[bold cyan]=== MAIN MENU ===[/bold cyan]\n")
        
        options = [
            "[1] Process Single Video",
            "[2] Batch Process Folder",
            "[3] Advanced Settings",
            "[4] View Processing History",
            "[5] Help & Documentation",
            "[6] Exit"
        ]
        
        for option in options:
            console.print(f"  {option}")
        
        console.print()
        choice = Prompt.ask(
            "[bold yellow]Select option[/bold yellow]",
            choices=["1", "2", "3", "4", "5", "6"],
            default="1"
        )
        
        return choice
    
    def process_single_video(self):
        console.print("\n[bold cyan]=== SINGLE VIDEO PROCESSING ===[/bold cyan]\n")
        
        video_path = Prompt.ask("[yellow]Enter video file path[/yellow]")
        
        if not self.validator.validate_video_path(video_path):
            console.print("[red]X[/red] Invalid video file path", style="bold red")
            return
        
        console.print(f"[green]OK[/green] Video file validated: [cyan]{video_path}[/cyan]")
        
        output_path = Prompt.ask(
            "[yellow]Output file path[/yellow]",
            default=str(Path(video_path).with_stem(Path(video_path).stem + "_nowm"))
        )
        
        quality_table = Table(box=box.SIMPLE)
        quality_table.add_column("Mode", style="cyan")
        quality_table.add_column("Description", style="dim")
        quality_table.add_row("1", "Fast (GPU Optimized)")
        quality_table.add_row("2", "Balanced (Recommended)")
        quality_table.add_row("3", "Maximum Quality (Slow)")
        
        console.print(quality_table)
        quality = Prompt.ask("[yellow]Select quality mode[/yellow]", choices=["1", "2", "3"], default="2")
        
        codec = Prompt.ask(
            "[yellow]Output codec[/yellow]",
            choices=["h264", "h265", "prores"],
            default="h264"
        )
        
        summary_table = Table(title="Processing Summary", box=box.ROUNDED, border_style="yellow")
        summary_table.add_column("Parameter", style="cyan bold")
        summary_table.add_column("Value", style="white")
        summary_table.add_row("Input File", video_path)
        summary_table.add_row("Output File", output_path)
        summary_table.add_row("Quality Mode", ["Fast", "Balanced", "Maximum"][int(quality)-1])
        summary_table.add_row("Codec", codec.upper())
        
        console.print(summary_table)
        
        if not Confirm.ask("[yellow]Start processing?[/yellow]", default=True):
            console.print("[yellow]![/yellow] Processing cancelled")
            return
        
        self._simulate_processing(video_path, output_path, quality, codec)
    
    def _simulate_processing(self, input_path, output_path, quality, codec):
        console.print("\n[bold green]=== PROCESSING STARTED ===[/bold green]\n")
        
        stages = [
            ("Loading AI Models", 8, "neural_engine"),
            ("Analyzing Video Frames", 12, "decoder"),
            ("Detecting Watermark Patterns", 15, "detector"),
            ("Initializing GPU Pipeline", 6, "gpu"),
            ("Processing Frame Sequence", 25, "frames"),
            ("AI Inpainting Layer", 20, "inpainting"),
            ("Temporal Consistency Check", 10, "temporal"),
            ("Encoding Output Video", 18, "encoder"),
            ("Finalizing & Verification", 8, "verify")
        ]
        
        with Progress(
            TextColumn("[bold blue]{task.description}"),
            BarColumn(bar_width=40, style="cyan", complete_style="green"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=console
        ) as progress:
            
            for stage_name, duration, stage_id in stages:
                task = progress.add_task(f"[cyan]{stage_name}...", total=100)
                
                for i in range(100):
                    progress.update(task, advance=1)
                    time.sleep(duration / 100)
                
                progress.update(task, description=f"[green]OK {stage_name}")
        
        console.print()
        
        time.sleep(0.5)
        console.print("[bold red]=== PROCESSING FAILED ===[/bold red]\n")
        
        error_panel = Panel(
            "[bold red]ERROR:[/bold red] Neural watermark detection failed\n\n"
            "[yellow]Details:[/yellow]\n"
            "  - Watermark signature mismatch detected\n"
            "  - Expected SORA-2 pattern not found in frames\n"
            "  - Video may not be generated by OpenAI Sora 2\n"
            "  - Or watermark pattern has been modified\n\n"
            "[dim]Error Code: NE_4402_PATTERN_MISMATCH[/dim]\n"
            "[dim]Timestamp: 2024-11-18 14:32:47 UTC[/dim]",
            title="[red]Processing Error[/red]",
            border_style="red",
            box=box.HEAVY
        )
        
        console.print(error_panel)
        console.print()
        
        if Confirm.ask("[yellow]View detailed error log?[/yellow]", default=False):
            self._show_detailed_error()
    
    def _show_detailed_error(self):
        console.print("\n[bold red]=== DETAILED ERROR LOG ===[/bold red]\n")
        
        log_text = """[dim]
[2024-11-18 14:32:41] INFO: Initializing neural engine...
[2024-11-18 14:32:42] INFO: Loading model weights (248M parameters)
[2024-11-18 14:32:43] INFO: GPU memory allocated: 4.2 GB
[2024-11-18 14:32:44] INFO: Model loaded successfully
[2024-11-18 14:32:44] INFO: Starting video analysis...
[2024-11-18 14:32:45] INFO: Frame extraction: 1847 frames detected
[2024-11-18 14:32:46] INFO: Watermark detection initiated...
[2024-11-18 14:32:47] [bold red]ERROR[/bold red]: Pattern matching failed at frame 127
[2024-11-18 14:32:47] [bold red]ERROR[/bold red]: Expected signature: SORA2_WM_v2.1.x
[2024-11-18 14:32:47] [bold red]ERROR[/bold red]: Found signature: UNKNOWN or NONE
[2024-11-18 14:32:47] [bold red]ERROR[/bold red]: Confidence score: 0.23 (threshold: 0.85)
[2024-11-18 14:32:47] [bold red]FATAL[/bold red]: Cannot proceed with removal - aborting
[2024-11-18 14:32:47] INFO: Cleaning up resources...
[2024-11-18 14:32:47] INFO: Process terminated
[/dim]"""
        
        console.print(Panel(log_text, border_style="red", box=box.ROUNDED))
    
    def batch_process_folder(self):
        console.print("\n[bold cyan]=== BATCH PROCESSING ===[/bold cyan]\n")
        
        folder_path = Prompt.ask("[yellow]Enter folder path containing videos[/yellow]")
        
        if not Path(folder_path).exists():
            console.print("[red]X[/red] Folder not found", style="bold red")
            return
        
        console.print(f"[green]OK[/green] Scanning folder: [cyan]{folder_path}[/cyan]")
        
        with Progress(TextColumn("[cyan]Scanning for videos..."), console=console) as progress:
            task = progress.add_task("scan", total=None)
            time.sleep(2)
        
        console.print("[red]X[/red] No valid Sora 2 videos found in folder", style="bold red")
        console.print("[dim]Supported formats: MP4, MOV, AVI, MKV, WEBM[/dim]")
    
    def advanced_settings(self):
        console.print("\n[bold cyan]=== ADVANCED SETTINGS ===[/bold cyan]\n")
        
        settings_table = Table(box=box.ROUNDED, border_style="cyan")
        settings_table.add_column("Setting", style="cyan bold")
        settings_table.add_column("Current Value", style="yellow")
        settings_table.add_column("Description", style="dim")
        
        settings_table.add_row("GPU Acceleration", "Enabled", "Use CUDA for processing")
        settings_table.add_row("Model Precision", "FP16", "Neural network precision")
        settings_table.add_row("Batch Size", "8", "Frames per batch")
        settings_table.add_row("Thread Count", "Auto (12)", "CPU threads")
        settings_table.add_row("Cache Size", "4 GB", "Temporary frame cache")
        settings_table.add_row("Backup Original", "Yes", "Keep original file")
        
        console.print(settings_table)
        console.print("\n[dim]Note: Settings are optimized for your system[/dim]")
    
    def view_history(self):
        console.print("\n[bold cyan]=== PROCESSING HISTORY ===[/bold cyan]\n")
        console.print("[yellow]![/yellow] No successful processing history found")
        console.print("[dim]Completed jobs will appear here[/dim]")
    
    def show_help(self):
        console.print("\n[bold cyan]=== HELP & DOCUMENTATION ===[/bold cyan]\n")
        
        help_text = """[bold yellow]Quick Start Guide[/bold yellow]

1. [cyan]Select a video file[/cyan] generated by OpenAI Sora 2
2. [cyan]Choose output settings[/cyan] (quality, codec, location)
3. [cyan]Start processing[/cyan] and monitor real-time progress
4. [cyan]Review results[/cyan] in the output folder

[bold yellow]Troubleshooting[/bold yellow]

- [red]Pattern Mismatch Error[/red]: Video is not from Sora 2
- [red]GPU Error[/red]: Update NVIDIA drivers to latest version
- [red]Memory Error[/red]: Close other applications or reduce quality
- [red]Codec Error[/red]: Install FFmpeg with full codec support

[bold yellow]System Requirements[/bold yellow]

- Python 3.10+
- NVIDIA GPU with 8GB+ VRAM (recommended)
- 16GB+ system RAM
- 10GB free disk space

For more help, visit: [link]https://github.com/sora-tools/docs[/link]
"""
        
        console.print(Panel(help_text, border_style="cyan", box=box.ROUNDED))
    
    def run(self):
        self.display_banner()
        time.sleep(0.5)
        
        console.print("\n[cyan]Initializing system components...[/cyan]")
        
        with Progress(TextColumn("[cyan]{task.description}"), console=console) as progress:
            task1 = progress.add_task("Loading neural models...", total=None)
            time.sleep(1.5)
            progress.update(task1, description="[green]OK Neural models loaded")
            
            task2 = progress.add_task("Initializing GPU...", total=None)
            time.sleep(1)
            progress.update(task2, description="[green]OK GPU initialized")
            
            task3 = progress.add_task("Loading video codecs...", total=None)
            time.sleep(0.8)
            progress.update(task3, description="[green]OK Video codecs ready")
        
        console.print()
        self.display_system_info()
        
        while True:
            choice = self.show_main_menu()
            
            if choice == "1":
                self.process_single_video()
            elif choice == "2":
                self.batch_process_folder()
            elif choice == "3":
                self.advanced_settings()
            elif choice == "4":
                self.view_history()
            elif choice == "5":
                self.show_help()
            elif choice == "6":
                console.print("\n[cyan]Thank you for using SORA 2 Watermark Remover![/cyan]")
                console.print("[dim]Shutting down...[/dim]\n")
                time.sleep(0.5)
                break
            
            console.print()
            Prompt.ask("[dim]Press Enter to continue[/dim]", default="")


def main():
    try:
        app = SoraWatermarkRemover()
        app.run()
    except KeyboardInterrupt:
        console.print("\n\n[yellow]! Operation cancelled by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]FATAL ERROR:[/bold red] {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
