class Vector:
  
  def __init__(self, vector_list):
      self.vector_data = vector_list
  
  def __str__(self):
      str_vector = ["("]
      for component in self.vector_data:
          str_vector.append(str(component))
      str_vector.append(")")
      return "".join(str_vector)
  
  def equals(self, vector_list):
      return self.vector_data == vector_list.get_data()
      
  
  def get_data(self):
      return self.vector_data
    
  def add(self, vector_list):
      str_vector = []
      if len(vector_list.get_data()) != len(self.vector_data):
          raise Exception("Length is not equal")
      for component in range(0,len(self.vector_data)):
          left_val = self.vector_data[component]
          right_val = vector_list.get_data()
          str_vector.append(left_val + right_val[component])
      
      return Vector(str_vector)
      
  def subtract(self, vector_list):
      str_vector = []
      if len(vector_list.get_data()) != len(self.vector_data):
          raise Exception("Length is not equal")
      for component in range(0,len(self.vector_data)):
          left_val = self.vector_data[component]
          right_val = vector_list.get_data()
          str_vector.append(left_val - right_val[component])
      
      return Vector(str_vector)
      
  def dot(self, vector_list):
      str_vector = []
      if len(vector_list.get_data()) != len(self.vector_data):
          raise Exception("Length is not equal")
      for component in range(0,len(self.vector_data)):
          left_val = self.vector_data[component]
          right_val = vector_list.get_data()
          sum_val = left_val * right_val[component]
          str_vector.append(sum_val)
      vector = Vector(str_vector).get_data()
      
      return sum(vector)
      
  def norm(self):
      pass
  
