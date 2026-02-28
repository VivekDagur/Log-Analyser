from  log_analyser import analyze_log

def test_stable_log(tmp_path):
    log_content = """[INFO] Server started
[INFO] Database connected
[INFO] User login
"""
    log_file = tmp_path / "stable.log"
    log_file.write_text(log_content)

    result = analyze_log(log_file)

    assert result["errors"] == 0
    assert result["warnings"] == 0
    assert result["info"] == 3
    assert result["total"] == 3
    assert result["error_rate"] == 0.0
    assert result["status"] == "SYSTEM HEALTHY"
    
def test_critical_log(tmp_path):
    log_content = """[ERROR] Failure
[ERROR] Crash
[INFO] Started
"""
    log_file = tmp_path / "critical.log"
    log_file.write_text(log_content)

    result = analyze_log(log_file)

    assert result["errors"] == 2
    assert result["warnings"] == 0
    assert result["info"] == 1
    assert result["total"] == 3
    assert result["error_rate"] > 20
    assert result["status"] == "SYSTEM CRITICAL"

def test_boundary_threshold(tmp_path):
    log_content = """[ERROR] Failure
[INFO] Start
[INFO] Run
[INFO] Stop
[INFO] End
"""
    log_file = tmp_path / "boundary.log"
    log_file.write_text(log_content)

    result = analyze_log(log_file)
    assert result["error_rate"] == 20.0
    assert result["status"] == "SYSTEM DEGRADED"

def test_mixed_safe_log(tmp_path):
    log_content = """[WARNING] Slow response
[INFO] Start
[ERROR] Minor glitch
[INFO] Continue
[INFO] Done
"""
    log_file = tmp_path / "mixed.log"
    log_file.write_text(log_content)

    result = analyze_log(log_file)

    assert result["errors"] == 1
    assert result["warnings"] == 1
    assert result["info"] == 3
    assert result["total"] == 5
    assert result["error_rate"] == 20.0
    assert result["status"] == "SYSTEM DEGRADED"

def test_empty_log(tmp_path):
    log_file = tmp_path / "empty.log"
    log_file.write_text("")

    result = analyze_log(log_file)

    assert result["errors"] == 0
    assert result["warnings"] == 0
    assert result["info"] == 0
    assert result["total"] == 0
    assert result["error_rate"] == 0.0
    assert result["status"] == "SYSTEM EMPTY"
