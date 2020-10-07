from rest_framework import permissions 

class UpdateOwnProfile(permissions.BasePermission):
  """Allow users to update their profile"""

  def has_object_permission(self, request, view, obj):
    """Check if user is trying to update own profile"""
    if request.method in permissions.SAFE_METHODS:
      return True
    
    return obj.id == request.user.id 