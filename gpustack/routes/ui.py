import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


class StaticFilesWithIndex(StaticFiles):
    """Custom StaticFiles that serves index.html for directory requests"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def get_response(self, path: str, scope):
        
        # Check if this looks like a directory request (with or without trailing slash)
        # FastAPI might strip trailing slashes, so we need to check both cases
        dir_path = path if path.endswith('/') else path + '/'
        
        # Construct the full filesystem path
        full_path = os.path.join(self.directory, dir_path)
        if os.path.isdir(full_path):
            index_path = dir_path + 'index.html'
            try:
                return await super().get_response(index_path, scope)
            except Exception as e:
                # If index.html doesn't exist, fall back to original behavior
                pass
        
        # For non-directory requests, use the original behavior
        return await super().get_response(path, scope)


def register(app: FastAPI):
    ui_dir = "/ui"
    if not os.path.isdir(ui_dir):
        raise RuntimeError(f"directory '{ui_dir}' does not exist")

    for name in ["css", "js", "static"]:
        app.mount(
            f"/{name}",
            StaticFiles(directory=os.path.join(ui_dir, name)),
            name=name,
        )

    # Mount the site directory for user-guide
    site_dir = "/manual"
    if os.path.isdir(site_dir):
        app.mount("/manual", StaticFilesWithIndex(directory=site_dir), name="manual")

    @app.get("/", include_in_schema=False)
    async def index():
        return FileResponse(os.path.join(ui_dir, "index.html"))
