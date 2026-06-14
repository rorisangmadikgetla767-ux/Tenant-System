const STORAGE_KEY ='tenantTrackerData';

function getAppData(){
    const raw = localStorage.getItem(STORAGE_KEY)
    if (!raw) {
        return {tenants: [] };
    }
    return JSON.parse(raw);
}

function saveAppData(data) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
}

function getTenants() {
    return getAppData.tenants;
}

function saveTenants(tenants =) {
    const data = getAppData();
    data.tenants = tenants
}