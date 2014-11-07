class Cabin < ActiveRecord::Base
	belongs_to :user
	has_many :posts
	validates :user, presence: true
end
