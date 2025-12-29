LIGHT_QSS = r"""
QWidget {
    background: #F5F5F7;
    color: #111827;
    font-family: "Segoe UI";
    font-size: 13px;
}

QLabel, QLabel * {
    background: transparent !important;
    border: none;
}

QLabel#Title {
    font-size: 20px;
    font-weight: 800;
    color: #0B1220;
}
QLabel#Subtitle { color: #556070; }
QLabel#Hint { color: #667085; }
QLabel#FileName { font-size: 14px; font-weight: 800; color: #0B1220; }
QLabel#FilePath { color: #556070; }

QPushButton:focus, QSpinBox:focus { outline: none; }

QFrame#Card {
    background: #FFFFFF;
    border: 1px solid rgba(17, 24, 39, 0.08);
    border-radius: 18px;
}

QFrame#DropZone {
    background: #FFFFFF;
    border: 2px dashed rgba(17, 24, 39, 0.18);
    border-radius: 22px;
}
QFrame#DropZone[active="true"] {
    border: 2px dashed rgba(10, 132, 255, 0.65);
}
QFrame#DropZone * { background: transparent !important; }

QLabel#DropTitle { font-weight: 900; }

QPushButton#Pill {
    background: rgba(17, 24, 39, 0.04);
    border: 1px solid rgba(17, 24, 39, 0.10);
    border-radius: 999px;
    padding: 10px 16px;
    min-height: 42px;
    font-weight: 800;
    color: #111827;
}
QPushButton#Pill:hover {
    background: rgba(10, 132, 255, 0.08);
    border: 1px solid rgba(10, 132, 255, 0.22);
}
QPushButton#Pill:pressed { background: rgba(17, 24, 39, 0.08); }
QPushButton#Pill:disabled {
    color: rgba(17, 24, 39, 0.35);
    background: rgba(17, 24, 39, 0.03);
    border: 1px solid rgba(17, 24, 39, 0.06);
}

QPushButton#PrimaryPill {
    background: #0A84FF;
    border: 1px solid #0A84FF;
    border-radius: 999px;
    padding: 10px 18px;
    min-height: 42px;
    font-weight: 900;
    color: #FFFFFF;
}
QPushButton#PrimaryPill:hover { background: #0077EE; border: 1px solid #0077EE; }
QPushButton#PrimaryPill:pressed { background: #0066D0; border: 1px solid #0066D0; }
QPushButton#PrimaryPill:disabled {
    background: rgba(17, 24, 39, 0.06);
    border: 1px solid rgba(17, 24, 39, 0.10);
    color: rgba(17, 24, 39, 0.35);
}

QPushButton#IconToggle {
    background: rgba(17, 24, 39, 0.03);
    border: 1px solid rgba(17, 24, 39, 0.08);
    border-radius: 999px;
    min-width: 42px;
    min-height: 42px;
    font-size: 18px;
    padding: 0px;
}
QPushButton#IconToggle:hover { background: rgba(17, 24, 39, 0.06); }
QPushButton#IconToggle:pressed { background: rgba(17, 24, 39, 0.10); }

QSpinBox#PagesSpin {
    background: #FFFFFF;
    border: 1px solid rgba(17, 24, 39, 0.10);
    border-radius: 16px;
    padding: 7px 12px;
    min-height: 40px;
    min-width: 90px;
    font-weight: 900;
    color: #111827;
}
QSpinBox#PagesSpin:hover { border: 1px solid rgba(17, 24, 39, 0.16); }

QPushButton#StepBtn {
    background: rgba(17, 24, 39, 0.04);
    border: 1px solid rgba(17, 24, 39, 0.10);
    border-radius: 12px;
    min-width: 40px;
    min-height: 18px;
    font-weight: 900;
    color: #556070;
    padding: 0px;
}
QPushButton#StepBtn:hover {
    background: rgba(10, 132, 255, 0.08);
    border: 1px solid rgba(10, 132, 255, 0.22);
    color: #0A84FF;
}
QPushButton#StepBtn:pressed {
    background: rgba(17, 24, 39, 0.08);
}
QPushButton#StepBtn:disabled {
    color: rgba(17, 24, 39, 0.30);
    background: rgba(17, 24, 39, 0.03);
    border: 1px solid rgba(17, 24, 39, 0.06);
}

QProgressBar {
    background: #FFFFFF;
    border: 1px solid rgba(17, 24, 39, 0.10);
    border-radius: 16px;
    height: 18px;
    text-align: center;
    color: rgba(17, 24, 39, 0.55);
    font-weight: 700;
}
QProgressBar::chunk {
    background: #0A84FF;
    border-radius: 16px;
}
"""

DARK_QSS = r"""
/* ===== Base ===== */
QWidget {
    background: #0B0B0F;
    color: #E8EEF7;
    font-family: "Segoe UI";
    font-size: 13px;
}

QLabel, QLabel * {
    background: transparent !important;
    border: none;
}

QLabel#Title {
    font-size: 20px;
    font-weight: 800;
    color: #F3F7FF;
}
QLabel#Subtitle { color: rgba(232, 238, 247, 0.72); }
QLabel#Hint { color: rgba(232, 238, 247, 0.65); }
QLabel#FileName { font-size: 14px; font-weight: 800; color: #F3F7FF; }
QLabel#FilePath { color: rgba(232, 238, 247, 0.72); }

QPushButton:focus, QSpinBox:focus { outline: none; }

QFrame#Card {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 18px;
}

QFrame#DropZone {
    background: rgba(255, 255, 255, 0.04);
    border: 2px dashed rgba(255, 255, 255, 0.16);
    border-radius: 22px;
}
QFrame#DropZone[active="true"] {
    border: 2px dashed rgba(122, 162, 255, 0.65);
}
QFrame#DropZone * { background: transparent !important; }

QLabel#DropTitle { font-weight: 900; }

QPushButton#Pill {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 999px;
    padding: 10px 16px;
    min-height: 42px;
    font-weight: 800;
    color: #E8EEF7;
}
QPushButton#Pill:hover {
    background: rgba(122, 162, 255, 0.14);
    border: 1px solid rgba(122, 162, 255, 0.22);
}
QPushButton#Pill:pressed { background: rgba(255, 255, 255, 0.10); }
QPushButton#Pill:disabled {
    color: rgba(232, 238, 247, 0.35);
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
}

QPushButton#PrimaryPill {
    background: #0A84FF;
    border: 1px solid #0A84FF;
    border-radius: 999px;
    padding: 10px 18px;
    min-height: 42px;
    font-weight: 900;
    color: #FFFFFF;
}
QPushButton#PrimaryPill:hover { background: #0077EE; border: 1px solid #0077EE; }
QPushButton#PrimaryPill:pressed { background: #0066D0; border: 1px solid #0066D0; }
QPushButton#PrimaryPill:disabled {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.10);
    color: rgba(232, 238, 247, 0.35);
}

QPushButton#IconToggle {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 999px;
    min-width: 42px;
    min-height: 42px;
    font-size: 18px;
    padding: 0px;
}
QPushButton#IconToggle:hover { background: rgba(255, 255, 255, 0.09); }
QPushButton#IconToggle:pressed { background: rgba(255, 255, 255, 0.12); }

QSpinBox#PagesSpin {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 16px;
    padding: 7px 12px;
    min-height: 40px;
    min-width: 90px;
    font-weight: 900;
    color: #E8EEF7;
}
QSpinBox#PagesSpin:hover { border: 1px solid rgba(255, 255, 255, 0.16); }

QPushButton#StepBtn {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 12px;
    min-width: 40px;
    min-height: 18px;
    font-weight: 900;
    color: rgba(232, 238, 247, 0.70);
    padding: 0px;
}
QPushButton#StepBtn:hover {
    background: rgba(122, 162, 255, 0.14);
    border: 1px solid rgba(122, 162, 255, 0.22);
    color: #7AA2FF;
}
QPushButton#StepBtn:pressed {
    background: rgba(255, 255, 255, 0.10);
}
QPushButton#StepBtn:disabled {
    color: rgba(232, 238, 247, 0.30);
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
}

QProgressBar {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 16px;
    height: 18px;
    text-align: center;
    color: rgba(232, 238, 247, 0.65);
    font-weight: 700;
}
QProgressBar::chunk {
    background: #0A84FF;
    border-radius: 16px;
}
"""
