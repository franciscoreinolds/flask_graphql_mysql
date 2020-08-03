# app/graphql/mutations/Profile/ProfileMutation.py

import graphene
from app import db

# Objects

from app.graphql.objects.ProfileObject import Profile as Profile
from app.graphql.objects.SkillInputObject import SkillInput as SkillInput

# Models

from app.models.Skill import Skill as SkillModel
from app.models.Profile import Profile as ProfileModel

class ProfileMutation(graphene.Mutation):
    class Arguments:
        role = graphene.String(required=True)
        description = graphene.String(required=True)
        user_id = graphene.Int(required=True)
        skills = graphene.List(SkillInput)
        id = graphene.Int()

    profile = graphene.Field(lambda: Profile)

    def mutate(self, info, role, description, user_id, skills):
        user = UserModel.query.get(user_id)

        profile = ProfileModel(role=role, description=description)
        # Create skills
        skill_list = [SkillModel(name=input_skill.name, score=input_skill.score) for input_skill in skills]
        profile.skills.extend(skill_list)

        db.session.add(profile)

        # Update user
        user.profile = profile

        db.session.commit()

        return ProfileMutation(profile=profile)
