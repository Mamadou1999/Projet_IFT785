from services.jobmatchobserver import JobMatchObserver
from services.profilviewsobserver import ProfileViewObserver
from services.developer import Developer
from services.jobposting import JobPosting

def test_job_match_observer_notification(developer_data):
    """
        Vérifie que l'observateur de match d'emploi est correctement notifié
    """
    dev = Developer(**developer_data)
    job = JobPosting(title="Python Dev")
    observer = JobMatchObserver()

    result = observer.update({"developer": dev, "job": job})
    
    assert "matched" in result.lower()
    assert dev.email in result

def test_profile_view_observer_notification(developer_data):
    """
        Vérifie que l'observateur de vue de profil est correctement notifié
    """
    dev = Developer(**developer_data)
    observer = ProfileViewObserver()

    result = observer.update({"profile": dev})
    
    assert "viewed" in result.lower()
    assert dev.email in result
