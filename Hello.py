def handle_event(event, context):
    try:
        print "Hello yal"
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": e.message}